This module contains a demo for parsing all gflags in a built executable.

To get started with this repository, follow these steps:

1. Install gflags and glogs. See [homebrew gflag](https://formulae.brew.sh/formula/gflags) and [homebrew glog](https://formulae.brew.sh/formula/glog).
    ```
    brew install gflags
    brew install glog
    ```

2. Build the project.
    ```
    mkdir build
    cd build
    cmake ./../ -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    make
    ./gflag_parser
    ```
    
    To make sure VSCode can properly recognize the include paths, execute the following in the project source folder after a successful build.

    ```
    ln -s build/compile_commands.json
    ```

3. Run the executable with different flag options.

   ```
   ./gflag_parser --help
   ``` 

4. To save all flag info into a xml file.

    ```
    ./gflag_parser --helpxml > ./../flags.xml
    ```

5. Parse the xml file into a json file.

    ```
    python3 parse_flags.py -i flags.xml
    ```
