# importing from a module
if False:
    from mymodule import my_func
    my_func()

# importing a module from a package
from MyMainPackage import some_main_script
from MyMainPackage.Subpackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()
