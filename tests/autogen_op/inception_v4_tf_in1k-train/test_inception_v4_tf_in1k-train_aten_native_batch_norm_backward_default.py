# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.native_batch_norm_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/inception_v4.tf_in1k-train", "aten.native_batch_norm_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 256, 8, 8]> grad_out = ?",
            "Tensor<[1, 256, 8, 8]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> running_mean = ?",
            "Optional[Tensor]<[256]> running_var = ?",
            "Optional[Tensor]<[256]> save_mean = ?",
            "Optional[Tensor]<[256]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 512, 8, 8]> grad_out = ?",
            "Tensor<[1, 512, 8, 8]> input = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> running_mean = ?",
            "Optional[Tensor]<[512]> running_var = ?",
            "Optional[Tensor]<[512]> save_mean = ?",
            "Optional[Tensor]<[512]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 448, 8, 8]> grad_out = ?",
            "Tensor<[1, 448, 8, 8]> input = ?",
            "Optional[Tensor]<[448]> weight = ?",
            "Optional[Tensor]<[448]> running_mean = ?",
            "Optional[Tensor]<[448]> running_var = ?",
            "Optional[Tensor]<[448]> save_mean = ?",
            "Optional[Tensor]<[448]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 384, 8, 8]> grad_out = ?",
            "Tensor<[1, 384, 8, 8]> input = ?",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> running_mean = ?",
            "Optional[Tensor]<[384]> running_var = ?",
            "Optional[Tensor]<[384]> save_mean = ?",
            "Optional[Tensor]<[384]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 320, 8, 8]> grad_out = ?",
            "Tensor<[1, 320, 8, 8]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> running_mean = ?",
            "Optional[Tensor]<[320]> running_var = ?",
            "Optional[Tensor]<[320]> save_mean = ?",
            "Optional[Tensor]<[320]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 320, 17, 17]> grad_out = ?",
            "Tensor<[1, 320, 17, 17]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> running_mean = ?",
            "Optional[Tensor]<[320]> running_var = ?",
            "Optional[Tensor]<[320]> save_mean = ?",
            "Optional[Tensor]<[320]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 17, 17]> grad_out = ?",
            "Tensor<[1, 256, 17, 17]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> running_mean = ?",
            "Optional[Tensor]<[256]> running_var = ?",
            "Optional[Tensor]<[256]> save_mean = ?",
            "Optional[Tensor]<[256]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 192, 8, 8]> grad_out = ?",
            "Tensor<[1, 192, 8, 8]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> running_mean = ?",
            "Optional[Tensor]<[192]> running_var = ?",
            "Optional[Tensor]<[192]> save_mean = ?",
            "Optional[Tensor]<[192]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 192, 17, 17]> grad_out = ?",
            "Tensor<[1, 192, 17, 17]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> running_mean = ?",
            "Optional[Tensor]<[192]> running_var = ?",
            "Optional[Tensor]<[192]> save_mean = ?",
            "Optional[Tensor]<[192]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 128, 17, 17]> grad_out = ?",
            "Tensor<[1, 128, 17, 17]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> running_mean = ?",
            "Optional[Tensor]<[128]> running_var = ?",
            "Optional[Tensor]<[128]> save_mean = ?",
            "Optional[Tensor]<[128]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 224, 17, 17]> grad_out = ?",
            "Tensor<[1, 224, 17, 17]> input = ?",
            "Optional[Tensor]<[224]> weight = ?",
            "Optional[Tensor]<[224]> running_mean = ?",
            "Optional[Tensor]<[224]> running_var = ?",
            "Optional[Tensor]<[224]> save_mean = ?",
            "Optional[Tensor]<[224]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 384, 17, 17]> grad_out = ?",
            "Tensor<[1, 384, 17, 17]> input = ?",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> running_mean = ?",
            "Optional[Tensor]<[384]> running_var = ?",
            "Optional[Tensor]<[384]> save_mean = ?",
            "Optional[Tensor]<[384]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 224, 35, 35]> grad_out = ?",
            "Tensor<[1, 224, 35, 35]> input = ?",
            "Optional[Tensor]<[224]> weight = ?",
            "Optional[Tensor]<[224]> running_mean = ?",
            "Optional[Tensor]<[224]> running_var = ?",
            "Optional[Tensor]<[224]> save_mean = ?",
            "Optional[Tensor]<[224]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 192, 35, 35]> grad_out = ?",
            "Tensor<[1, 192, 35, 35]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> running_mean = ?",
            "Optional[Tensor]<[192]> running_var = ?",
            "Optional[Tensor]<[192]> save_mean = ?",
            "Optional[Tensor]<[192]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 96, 35, 35]> grad_out = ?",
            "Tensor<[1, 96, 35, 35]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> running_mean = ?",
            "Optional[Tensor]<[96]> running_var = ?",
            "Optional[Tensor]<[96]> save_mean = ?",
            "Optional[Tensor]<[96]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 64, 35, 35]> grad_out = ?",
            "Tensor<[1, 64, 35, 35]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> running_mean = ?",
            "Optional[Tensor]<[64]> running_var = ?",
            "Optional[Tensor]<[64]> save_mean = ?",
            "Optional[Tensor]<[64]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 96, 71, 71]> grad_out = ?",
            "Tensor<[1, 96, 71, 71]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> running_mean = ?",
            "Optional[Tensor]<[96]> running_var = ?",
            "Optional[Tensor]<[96]> save_mean = ?",
            "Optional[Tensor]<[96]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 64, 73, 73]> grad_out = ?",
            "Tensor<[1, 64, 73, 73]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> running_mean = ?",
            "Optional[Tensor]<[64]> running_var = ?",
            "Optional[Tensor]<[64]> save_mean = ?",
            "Optional[Tensor]<[64]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 96, 73, 73]> grad_out = ?",
            "Tensor<[1, 96, 73, 73]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> running_mean = ?",
            "Optional[Tensor]<[96]> running_var = ?",
            "Optional[Tensor]<[96]> save_mean = ?",
            "Optional[Tensor]<[96]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 64, 147, 147]> grad_out = ?",
            "Tensor<[1, 64, 147, 147]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> running_mean = ?",
            "Optional[Tensor]<[64]> running_var = ?",
            "Optional[Tensor]<[64]> save_mean = ?",
            "Optional[Tensor]<[64]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 147, 147]> grad_out = ?",
            "Tensor<[1, 32, 147, 147]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> running_mean = ?",
            "Optional[Tensor]<[32]> running_var = ?",
            "Optional[Tensor]<[32]> save_mean = ?",
            "Optional[Tensor]<[32]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 149, 149]> grad_out = ?",
            "Tensor<[1, 32, 149, 149]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> running_mean = ?",
            "Optional[Tensor]<[32]> running_var = ?",
            "Optional[Tensor]<[32]> save_mean = ?",
            "Optional[Tensor]<[32]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.native_batch_norm_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.native_batch_norm_backward.default", input_strings
    )
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False

    if metric["native_run"] == True:
        result_after = None
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            ttnn.graph.begin_graph_capture()
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False
        finally:
            trace = ttnn.graph.end_graph_capture()
            call_stack = ttnn.graph.extract_calltrace(trace)
            if metric["run"] == True:
                print(call_stack)
                expected_to_host_count = 0
                if result_after is None:
                    expected_to_host_count = 0
                elif isinstance(result_after, torch.Tensor):
                    expected_to_host_count = 1
                elif isinstance(result_after, (list, dict)):
                    expected_to_host_count = len(result_after)
                else:
                    print(f"Unexpected result_after type: {type(result_after)}")

                to_host_count = sum(["Tensor::cpu" in str(node) for node in call_stack])
                fallbacks_to_host_count = to_host_count - expected_to_host_count
                print(f"expected_to_host_count: {expected_to_host_count}")
                print(f"to_host_count: {to_host_count}")
                print(f"fallbacks_to_host_count: {fallbacks_to_host_count}")
                metric["ttnn_fallbacks_to_host_count"] = fallbacks_to_host_count

    if metric["run"] == True:
        try:
            # Check inference result
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if not any(["aten." in str(node.target) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
