#include "bar_flags.h"

#include <gflags/gflags.h>

DEFINE_bool(bar_flag_bool, false, "Bar component's boolean flag.");
DEFINE_int32(bar_flag_int, 0, "Bar component's integer flag.");
DEFINE_double(bar_flag_double, 0.0, "Bar component's double flag.");
