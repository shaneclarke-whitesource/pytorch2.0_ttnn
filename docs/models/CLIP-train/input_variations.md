# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._softmax_backward_data.default     |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._to_copy.default                   |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten._unsafe_view.default               |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor                         |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.addmm.default                      |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.argmax.default                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.bmm.default                        |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cat.default                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.clone.default                      |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.detach.default                     |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.div.Tensor                         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.embedding.default                  |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.embedding_dense_backward.default   |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.eq.Scalar                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.exp.default                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.expand.default                     |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.full.default                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.index.Tensor                       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.index_put.default                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.linalg_vector_norm.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.masked_fill.Scalar                 |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.mm.default                         |                 20 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.mul.Tensor                         |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.native_layer_norm.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.native_layer_norm_backward.default |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.neg.default                        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.new_zeros.default                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.rsub.Scalar                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.select.int                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.select_backward.default            |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.sigmoid.default                    |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.sigmoid_backward.default           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.slice.Tensor                       |                 10 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.slice_backward.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.sum.default                        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 38 | aten.sum.dim_IntList                    |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 39 | aten.t.default                          |                 16 |           0 |         0 |          0 | ✘           |       0 |
| 40 | aten.transpose.int                      |                 12 |           0 |         0 |          0 | ✘           |       0 |
| 41 | aten.unsqueeze.default                  |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 42 | aten.view.default                       |                 29 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999583 |      0 |
|  1 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Unknown  | Done       | 0.999549 |      0 |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[12, 50, 50]> grad_output = ?,<br>Tensor<[12, 50, 50]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[16, 7, 7]> grad_output = ?,<br>Tensor<[16, 7, 7]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | Unknown  | Fallback   |     1 |     -1 |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Unknown  | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, 7, 64]    | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Unknown  | Done       | 0.999999 |      0 |
|  3 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?           | Unknown  | Done       | 0.999998 |      0 |
|  4 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Unknown  | Done       | 0.999998 |      0 |
|  5 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
|  6 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  7 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?     | Unknown  | Done       | 0.999998 |      0 |
|  8 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?   | Unknown  | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Unknown  | Done       | 0.999971 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.999967 |      0 |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Unknown  | Done       | 0.999955 |      0 |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Unknown  | Done       | 0.99997  |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.999943 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999966 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | Unknown  | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ? | Unknown  | Done       | 0.999986 |      0 |
|  1 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Unknown  | Done       | 0.999986 |      0 |
|  2 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ? | Unknown  | Done       | 0.999986 |      0 |
|  3 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?    | Unknown  | Done       | 0.999991 |      0 |
|  4 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?   | Unknown  | Done       | 0.999985 |      0 |
|  5 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?    | Unknown  | Done       | 0.999991 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[12, 50, 50]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[16, 7, 7]> self = ?                                                                | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Unknown  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Fallback   |     1 |     -1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 7, 7]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | Unknown  | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1]> self = ?        | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 50, 3072]> self = ? | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[12, 50, 50]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[16, 7, 7]> self = ?    | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[2, 1]> self = ?        | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[2, 7, 2048]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[]> self = ?            | Unknown  | Done       |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Unknown  | Done       | 0.999996 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Unknown  | Done       |     1 |      0 |
### aten.embedding_dense_backward.default
|    | ATen Input Variations                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>Tensor<[1, 50]> indices = ?,<br>int num_weights = 50,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False  | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 7, 512]> grad_output = ?,<br>Tensor<[1, 7]> indices = ?,<br>int num_weights = 77,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False    | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7, 512]> grad_output = ?,<br>Tensor<[2, 7]> indices = ?,<br>int num_weights = 49408,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False | Unknown  | Fallback   |     1 |     -1 |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2, 1]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?     | Unknown  | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Unknown  | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange, <[2]>] | Unknown  | Unknown    | N/A   | N/A    |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>],<br>Tensor<[2, 512]> values = ?,<br>bool accumulate = True | Unknown  | Fallback   |     1 |     -1 |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Fallback   |     1 |     -1 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> mask = ?,<br>number value = 0                                 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> mask = ?,<br>number value = 0                                 | Unknown  | Fallback   |     1 |     -1 |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?        | Unknown  | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?    | Unknown  | Done       | 0.999966 |      0 |
|  2 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?    | Unknown  | Done       | 0.999967 |      0 |
|  3 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ? | Unknown  | Done       | 0.999955 |      0 |
|  4 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Unknown  | Done       | 0.999972 |      0 |
|  5 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?   | Unknown  | Done       | 0.999972 |      0 |
|  6 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?        | Unknown  | Done       | 0.999996 |      0 |
|  7 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?      | Unknown  | Done       | 1        |      0 |
|  8 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?    | Unknown  | Done       | 0.999972 |      0 |
|  9 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?   | Unknown  | Done       | 0.999992 |      0 |
| 10 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?   | Unknown  | Done       | 0.999986 |      0 |
| 11 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.999945 |      0 |
| 12 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
| 13 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999968 |      0 |
| 14 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?   | Unknown  | Done       | 0.999991 |      0 |
| 15 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?    | Unknown  | Done       | 0.999991 |      0 |
| 16 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Unknown  | Done       | 0.999992 |      0 |
| 17 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?      | Unknown  | Done       | 0.999992 |      0 |
| 18 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?   | Unknown  | Done       | 0.999986 |      0 |
| 19 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?    | Unknown  | Done       | 0.999986 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?             | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Unknown  | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Unknown  | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125             | Unknown  | Done       | 1        |      0 |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Unknown  | Done       | 0.999996 |      0 |
|  5 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?               | Unknown  | Done       | 1        |      0 |
|  6 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?             | Unknown  | Done       | 0.999996 |      0 |
|  7 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | Unknown  | Fallback   | 1        |     -1 |
|  8 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Unknown  | Done       | 0.999996 |      0 |
|  9 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Unknown  | Done       | 0.999996 |      0 |
| 10 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Unknown  | Done       | 0.999996 |      0 |
| 11 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125              | Unknown  | Done       | 1        |      0 |
| 12 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                       | Unknown  | Fallback   | 1        |     -1 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Unknown  | Done       | N/A   |      1 |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | N/A   |      1 |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_out = ?,<br>Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 50, 1]> mean = ?,<br>Tensor<[1, 50, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | Unknown  | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 768]> grad_out = ?,<br>Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True]                 | Unknown  | Fallback   |     1 |      0 |
|  2 | Tensor<[2, 7, 512]> grad_out = ?,<br>Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Tensor<[2, 7, 1]> mean = ?,<br>Tensor<[2, 7, 1]> rstd = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | Unknown  | Fallback   |     1 |      0 |
### aten.neg.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2, 512]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 512]> self = ?,<br>List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0 | Unknown  | Done       | 0.999995 |      0 |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  | Done       |     1 |     -1 |
### aten.select_backward.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 1,<br>int index = 0 | Unknown  | Fallback   |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Unknown  | Done       | 0.999756 |      0 |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Unknown  | Done       | 0.999753 |      0 |
### aten.sigmoid_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 3072]> grad_output = ?,<br>Tensor<[1, 50, 3072]> output = ? | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 7, 2048]> grad_output = ?,<br>Tensor<[2, 7, 2048]> output = ?   | Unknown  | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 50                  | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Done       |     1 |     -1 |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 768],<br>int dim = 1,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1         | Unknown  | Fallback   |     1 |     -1 |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1]> self = ? | Unknown  | Fallback   |     1 |      0 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[14, 2048]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[14, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[2, 7, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True    | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[50, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[50, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | Unknown  | Fallback   | 1.0   | -1     |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?    | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[14, 2048]> self = ?  | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[14, 512]> self = ?   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[2, 1]> self = ?      | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[2, 512]> self = ?    | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[2048, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[3072, 768]> self = ? | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[50, 3072]> self = ?  | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[50, 768]> self = ?   | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[512, 1]> self = ?    | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[512, 2048]> self = ? | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[512, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[512, 768]> self = ?  | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[768, 3072]> self = ? | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[768, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[768, 768]> self = ?  | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[12, 50, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[12, 64, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[16, 64, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[16, 7, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[2, 7]> self = ?,<br>int dim = 1    | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Unknown  | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]            | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, 50, 64] | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]             | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]             | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64] | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]               | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]  | Unknown  | Done       |     1 |     -1 |
| 12 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Unknown  | Done       |     1 |     -1 |
| 13 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]               | Unknown  | Done       |     1 |     -1 |
| 14 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64] | Unknown  | Done       |     1 |     -1 |
| 15 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Unknown  | Done       |     1 |     -1 |
| 16 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Unknown  | Done       |     1 |     -1 |
| 17 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]    | Unknown  | Done       |     1 |     -1 |
| 18 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]      | Unknown  | Done       |     1 |     -1 |
| 19 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Unknown  | Done       |     1 |     -1 |
| 20 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Unknown  | Done       |     1 |     -1 |
| 21 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]   | Unknown  | Done       |     1 |     -1 |
| 22 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]    | Unknown  | Done       |     1 |     -1 |
| 23 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Unknown  | Done       |     1 |     -1 |
| 24 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Unknown  | Done       |     1 |     -1 |
| 25 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]   | Unknown  | Done       |     1 |     -1 |
| 26 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]      | Unknown  | Done       |     1 |     -1 |
| 27 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Unknown  | Done       |     1 |     -1 |
| 28 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Unknown  | Done       |     1 |     -1 |

