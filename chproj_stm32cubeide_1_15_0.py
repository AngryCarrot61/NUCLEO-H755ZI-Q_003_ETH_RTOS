'''
Changed the name of an STM32CubeIDE project:    
1. Rename directories and files:
   ./Nucleo-H7A3ZI-Q_SDMMC_QSPI_FT813_IOC_Leo.ioc -> ./Nucleo-H7A3ZI-Q_SDMMC_QSPI_FT813_Leo_Copy.ioc
2. Replace strings in files:
   ./Nucleo-H7A3ZI-Q_SDMMC_QSPI_FT813_IOC_Leo.ioc
   ./STM32CubeIDE/.cproject
   ./STM32CubeIDE/.project
'''
# Output:
# c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy>chproj_stm32cubeide.py
# Current dir     : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy
# .cproject       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.cproject
# .project        : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.project
# Name old        : Nucleo-H7A3ZI-Q_Leo
# Name new        : Nucleo-H7A3ZI-Q_Leo_Copy
# Rename directories and files:
# .ioc name old   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo.ioc
# .ioc name new   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy.ioc
# .launch name old   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo Debug.launch
# .launch name new   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy Debug.launch
# .elf name old   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo.elf
# .elf name new   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo_Copy.elf
# .list name old  : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo.list
# .list name new  : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo_Copy.list
# .map name old   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo.map
# .map name new   : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\STM32CubeIDE\Debug\Nucleo-H7A3ZI-Q_Leo_Copy.map
# Replace strings in files:
# .ioc            : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy.ioc
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy.ioc
# Changing        : "Nucleo-H7A3ZI-Q_Leo" to "Nucleo-H7A3ZI-Q_Leo_Copy"
# .cproject       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.cproject
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.cproject
# Changing        : "Nucleo-H7A3ZI-Q_Leo" to "Nucleo-H7A3ZI-Q_Leo_Copy"
# .project        : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.project
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.project
# Changing        : "Nucleo-H7A3ZI-Q_Leo" to "Nucleo-H7A3ZI-Q_Leo_Copy"
# .mxproject      : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.mxproject
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.mxproject
# "Nucleo-H7A3ZI-Q_Leo" not found
# .project        : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.project
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\.project
# Changing        : "Nucleo-H7A3ZI-Q_Leo" to "Nucleo-H7A3ZI-Q_Leo_Copy"
# .launch         : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy Debug.launch
# Modifying       : c:\STM32CubeIDE\Nucleo-H7A3ZI-Q_Leo_Copy\Nucleo-H7A3ZI-Q_Leo_Copy Debug.launch
# Changing        : "Nucleo-H7A3ZI-Q_Leo" to "Nucleo-H7A3ZI-Q_Leo_Copy"

import os
import sys

file_extensions = [
               '.ioc', 
               ]

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    print ('Modifying       : {filename}'.format(**locals()))
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print ('"{old_string}" not found'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print ('Changing        : "{old_string}" to "{new_string}"'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)

def main(argv):
    # Getting the current work directory (cwd)
    dir_current = os.getcwd()
    dir_current_split = dir_current.split('\\')
    n = len(dir_current_split)
    dst_dir = dir_current_split[n-1]
    new_name = dst_dir
    print ("Current dir     : " + dir_current)
    # Current dir     : c:\Users\jbk\STM32CubeIDE\FI3000_3
    print ("new_name        : " + new_name)
    # new_name        : FI3000_3
    
    old_name = ''
    for r, d, f in os.walk(dir_current):
        for file in f:
            # Get substring: last two character of the filename (.c or .h)
            position = file.rfind('.')
            ext = file[position:]
            for file_extension in file_extensions:
                if file_extension == ext:
                    old_name = file[:position]
                    print(file);
    print ("old_name        : " + old_name)
    # old_name        : FI3000_3

    filename_ioc_old = old_name + ".ioc"
    filename_ioc_new = new_name + ".ioc"
    print ("filename_ioc_old: " + filename_ioc_old)
    print ("filename_ioc_new: " + filename_ioc_new)
    # filename_ioc_old: Ja_FI3000_3.ioc
    # filename_ioc_new: FI3000_3.ioc
    
    if os.path.isfile(filename_ioc_old):
        # file exists
        os.rename(filename_ioc_old, filename_ioc_new)

    filename_cproject = '.cproject'
    filename_project = '.project'
    
    if os.path.isfile(filename_cproject):
        # file exists
        print (".cproject       : " + filename_cproject)
        inplace_change(filename_cproject, old_name, new_name)

    if os.path.isfile(filename_project):
        # file exists
        print (".project        : " + filename_project)
        inplace_change(filename_project, old_name, new_name)
   
    dir_debug = dir_current + '\\Debug'
    print ("dir_debug       : " + dir_debug)

    print ("removing        : ")
    for r, d, f in os.walk(dir_debug):
        for file in f:
            # Get substring: last two character of the filename (.c or .h)
            if old_name in file:
                file_to_remove = dir_debug + '\\' + file
                if os.path.isfile(file_to_remove):
                    print(file_to_remove);
                    os.remove(file_to_remove)


if __name__ == "__main__":
    #main(sys.argv[1:])
    
    main(sys.argv)
