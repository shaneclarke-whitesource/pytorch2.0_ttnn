import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import check_with_pcc


class AddMmModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, mat1, mat2):
        return torch.addmm(input, mat1, mat2)


@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4), (4, 4), (4, 4)]],
)
def test_addmm(device, input_shapes):
    m = AddMmModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.matmul) == 1
    assert target.count(ttnn.add) == 1
    assert target.index(ttnn.matmul) < target.index(ttnn.add)
    assert nodes[target.index(ttnn.add)].args[1].target == ttnn.matmul
    # Check inference result
    assert check_with_pcc(result_before, result_after)
