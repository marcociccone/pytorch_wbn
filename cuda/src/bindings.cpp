#include "lib_cffi.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("wbn_mean_var_cuda", &wbn_mean_var_cuda);
    m.def("wbn_forward_cuda", &wbn_forward_cuda);
    m.def("wbn_edz_eydz_cuda", &wbn_edz_eydz_cuda);
    m.def("wbn_backward_cuda", &wbn_backward_cuda);
}
