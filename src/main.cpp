#include <gflags/gflags.h>
#include <glog/logging.h>

#include "bar.h"
#include "foo.h"
#include "main_flags.h"

int main(int argc, char *argv[]) {
  gflags::SetUsageMessage("Demo of gflags.");
  gflags::ParseCommandLineFlags(&argc, &argv, true);

  Foo foo;
  Bar bar;

  LOG(INFO) << "Hello, World!" << std::endl;

  return 0;
}
