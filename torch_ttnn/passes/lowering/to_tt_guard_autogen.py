# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# THIS FILE IS AUTOGENERATED BY tools/generate_guard_function_from_input_var_metric.py
# DO NOT EDIT THIS FILE MANUALLY
# YOU CAN DEBUG THESE INPUT VAR VIA tests/autogen-op/ALL
import torch
import torch_ttnn.metrics as metrics
from functools import partial


aten__log_softmax_default_blocklist = [["Tensor<[19, 256008]> self = ?", "int dim = 1", "bool half_to_float = False"]]
aten__scaled_dot_product_flash_attention_default_blocklist = [
    ["Tensor<[1, 16, 197, 64]> query = ?", "Tensor<[1, 16, 197, 64]> key = ?", "Tensor<[1, 16, 197, 64]> value = ?"],
    ["Tensor<[1, 12, 197, 64]> query = ?", "Tensor<[1, 12, 197, 64]> key = ?", "Tensor<[1, 12, 197, 64]> value = ?"],
    ["Tensor<[1, 16, 50, 64]> query = ?", "Tensor<[1, 16, 50, 64]> key = ?", "Tensor<[1, 16, 50, 64]> value = ?"],
    ["Tensor<[1, 8, 4096, 40]> query = ?", "Tensor<[1, 8, 4096, 40]> key = ?", "Tensor<[1, 8, 4096, 40]> value = ?"],
    ["Tensor<[1, 8, 1024, 80]> query = ?", "Tensor<[1, 8, 9, 80]> key = ?", "Tensor<[1, 8, 9, 80]> value = ?"],
    ["Tensor<[1, 8, 256, 160]> query = ?", "Tensor<[1, 8, 256, 160]> key = ?", "Tensor<[1, 8, 256, 160]> value = ?"],
    ["Tensor<[1, 8, 64, 160]> query = ?", "Tensor<[1, 8, 64, 160]> key = ?", "Tensor<[1, 8, 64, 160]> value = ?"],
    ["Tensor<[1, 12, 50, 64]> query = ?", "Tensor<[1, 12, 50, 64]> key = ?", "Tensor<[1, 12, 50, 64]> value = ?"],
    ["Tensor<[1, 16, 1370, 80]> query = ?", "Tensor<[1, 16, 1370, 80]> key = ?", "Tensor<[1, 16, 1370, 80]> value = ?"],
    ["Tensor<[1, 12, 1, 64]> query = ?", "Tensor<[1, 12, 1, 64]> key = ?", "Tensor<[1, 12, 1, 64]> value = ?"],
    [
        "Tensor<[1, 12, 4, 64]> query = ?",
        "Tensor<[1, 12, 4, 64]> key = ?",
        "Tensor<[1, 12, 4, 64]> value = ?",
        "float dropout_p = 0.0",
        "bool is_causal = True",
    ],
]
aten_native_layer_norm_default_blocklist = [
    [
        "Tensor<[1, 9, 4096]> input = ?",
        "List[int] normalized_shape = [4096]",
        "Optional[Tensor]<[4096]> weight = ?",
        "Optional[Tensor]<[4096]> bias = ?",
        "float eps = 1e-12",
    ],
    [
        "Tensor<[1, 7, 4544]> input = ?",
        "List[int] normalized_shape = [4544]",
        "Optional[Tensor]<[4544]> weight = ?",
        "Optional[Tensor]<[4544]> bias = ?",
        "float eps = 1e-05",
    ],
]
aten_convolution_default_blocklist = [
    # TODO(#385): Guard and fallback (likely) OOM cases
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[1024, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[1024]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 64, 480, 640]> input = ?",
        "Tensor<[64, 64, 3, 3]> weight = ?",
        "Optional[Tensor]<[64]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 64, 480, 640]> input = ?",
        "Tensor<[1, 64, 3, 3]> weight = ?",
        "Optional[Tensor]<[1]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 384, 512]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 800, 1088]> input = ?",
        "Tensor<[64, 3, 7, 7]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [3, 3]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 100, 136]> input = ?",
        "Tensor<[819, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[819]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 50, 68]> input = ?",
        "Tensor<[819, 256, 3, 3]> weight = ?",
        "Optional[Tensor]<[819]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 720, 1280]> input = ?",
        "Tensor<[64, 3, 7, 7]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [3, 3]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 256, 180, 320]> input = ?",
        "Tensor<[512, 256, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 32, 32]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [32, 32]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[768, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 512, 672]> input = ?",
        "Tensor<[192, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[192]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 518, 518]> input = ?",
        "Tensor<[1280, 3, 14, 14]> weight = ?",
        "Optional[Tensor]<[1280]> bias = ?",
        "List[int] stride = [14, 14]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 3, 224, 224]> input = ?",
        "Tensor<[1024, 3, 16, 16]> weight = ?",
        "Optional[Tensor]<[1024]> bias = ?",
        "List[int] stride = [16, 16]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 528, 192, 192]> input = ?",
        "Tensor<[528, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 2",
    ],
    [
        "Tensor<[1, 1056, 96, 96]> input = ?",
        "Tensor<[1056, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 4",
    ],
    [
        "Tensor<[1, 2904, 48, 48]> input = ?",
        "Tensor<[2904, 264, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 11",
    ],
    [
        "Tensor<[1, 816, 19, 19]> input = ?",
        "Tensor<[816, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [2, 2]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 816",
    ],
    [
        "Tensor<[1, 816, 23, 23]> input = ?",
        "Tensor<[816, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 816",
    ],
    [
        "Tensor<[1, 960, 24, 24]> input = ?",
        "Tensor<[960, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [2, 2]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 960",
    ],
    [
        "Tensor<[1, 960, 27, 27]> input = ?",
        "Tensor<[960, 1, 5, 5]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 960",
    ],
    [
        "Tensor<[1, 768, 3000]> input = ?",
        "Tensor<[768, 768, 3]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "List[int] stride = [2]",
        "List[int] padding = [1]",
        "List[int] dilation = [1]",
        "bool transposed = False",
        "List[int] output_padding = [0]",
        "int groups = 1",
    ],
    [
        "Tensor<[1, 320, 64, 64]> input = ?",
        "Tensor<[320, 320, 3, 3]> weight = ?",
        "Optional[Tensor]<[320]> bias = ?",
        "List[int] stride = [1, 1]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
    # TODO(tt-metal#16173): weight_matrix_width_ntiles % weight_block_w_ntiles == 0
    [
        "Tensor<[1, 1232, 14, 14]> input = ?",
        "Tensor<[3024, 1232, 1, 1]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [0, 0]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 1",
    ],
]

aten_argmax_default_blocklist = [
    ["Tensor<[2, 7]> self = ?", "Optional[int] dim = -1"],
    ["Tensor<[1, 7]> self = ?", "Optional[int] dim = -1"],
    ["Tensor<[1, 51865]> self = ?", "Optional[int] dim = -1"],
]


def get_inputs(node):
    node_inputs = metrics.collect_input_variation_from_node(node)
    if type(node_inputs) == metrics.InputVariation:
        return node_inputs.inputs
    elif type(node_inputs) == metrics.ConvertedInput:
        return node_inputs.original_input_variation.inputs
    else:
        return None


def guard_aten(blocklist, node):
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blocklist:
        return False
    return True


GUARD = {
    torch.ops.aten._log_softmax.default: partial(guard_aten, aten__log_softmax_default_blocklist),
    torch.ops.aten._scaled_dot_product_flash_attention.default: partial(
        guard_aten, aten__scaled_dot_product_flash_attention_default_blocklist
    ),
    torch.ops.aten.native_layer_norm.default: partial(guard_aten, aten_native_layer_norm_default_blocklist),
    torch.ops.aten.convolution.default: partial(guard_aten, aten_convolution_default_blocklist),
    torch.ops.aten.argmax.default: partial(guard_aten, aten_argmax_default_blocklist),
}
