#include "foo_flags.h"

#include <gflags/gflags.h>

DEFINE_bool(foo_flag_bool, false, "Foo component's boolean flag.");
DEFINE_int32(foo_flag_int, 0, "Foo component's integer flag.");
DEFINE_string(foo_flag_string, "", "Foo component's string flag.");