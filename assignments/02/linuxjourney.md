# Exercises
### 1.
    $ date
    Wed Oct 23 17:46:40 2024
    $ whoami
    maehl
  
### 2.
No exercises for this lesson.

### 3.
Run the cd command without any flags, where does it take you?
To the home directory

### 4.
Run ls with different flags and see the output you receive.

ls -R: recursively list directory contents
ls -r: reverse order while sorting
ls -t: sort by modification time, newest first

I ran this in my root directory so the output was very long :)

### 5.
Create a new file
Note the timestamp
Touch the file and check the timestamp once again

    $ touch dis08
    $ ls -l
    Oct 23 17:59
    $ touch dis08
    $ ls -l
    Oct 23 18:00


### 6.
Run the file command on a few different directories and files and note the output.

    $ file desktop.ini
    desktop.ini: Unicode text, UTF-16, little-endian text, with CRLF line terminators
    $ file 3.zip
    3.zip: Zip archive data, at least v2.0 to extract, compression method=store

### 7.
Run cat on different files and directories. Then try to cat multiple files.

    $ cat desktop.ini
    [.ShellClassInfo]
    LocalizedResourceName=@%SystemRoot%\system32\windows.storage.dll,-21779
    InfoTip=@%SystemRoot%\system32\shell32.dll,-12688
    IconResource=%SystemRoot%\system32\imageres.dll,-113
    IconFile=%SystemRoot%\system32\shell32.dll
    IconIndex=-236

### 8.
Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.    
    $ less strings_de.xml

### 9.
Navigate through your previous command history with the Up and Down keys. Play around with ctrl-R reverse search.

## 10.
Copy over a couple of files, be careful not to overwrite anything important.

### 11.
Rename a file, then move that file to a different directory.

    $ mv strings_de.xml string_fr.xml
    $ string_fr.xml ../

### 12.
Make a couple of directories and move some files into that directory.

    $ mkdir new_strings test_strings
    $ mv string_fr.xml test_strings

### 13.
Create a file called -file (don't forget the dash!).
Remove that file.

    $ touch -- -file
    $ rm -- -file

### 14.
Find a file from the root directory that has the word net in it.

    $ find / -name net
    find: ‘/d/System Volume Information’: Permission denied
    
### 15.
Run help on the echo command, logout command and pwd command.

    maehl@DESKTOP-KFT9U41 MINGW64 /d/Pokemmo/pokemmo/data/strings
    $ pwd --help
    pwd: pwd [-LPW]
        Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links
      -W        print the Win32 value of the physical directory

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.

    maehl@DESKTOP-KFT9U41 MINGW64 /d/Pokemmo/pokemmo/data/strings
    $ help echo
    echo: echo [-neE] [arg ...]
        Write arguments to the standard output.

    Display the ARGs, separated by a single space character and followed by a
    newline, on the standard output.

    Options:
      -n        do not append a newline
      -e        enable interpretation of the following backslash escapes
      -E        explicitly suppress interpretation of backslash escapes

    `echo' interprets the following backslash-escaped characters:
      \a        alert (bell)
      \b        backspace
      \c        suppress further output
      \e        escape character
      \E        escape character
      \f        form feed
      \n        new line
      \r        carriage return
      \t        horizontal tab
      \v        vertical tab
      \\        backslash
      \0nnn     the character whose ASCII code is NNN (octal).  NNN can be
                0 to 3 octal digits
      \xHH      the eight-bit character whose value is HH (hexadecimal).  HH
                can be one or two hex digits
      \uHHHH    the Unicode character whose value is the hexadecimal value HHHH.
                HHHH can be one to four hex digits.
      \UHHHHHHHH the Unicode character whose value is the hexadecimal value
                HHHHHHHH. HHHHHHHH can be one to eight hex digits.

    Exit Status:
    Returns success unless a write error occurs.

    maehl@DESKTOP-KFT9U41 MINGW64 /d/Pokemmo/pokemmo/data/strings
    $ help logout
    logout: logout [n]
        Exit a login shell.

    Exits a login shell with exit status N.  Returns an error if not executed
    in a login shell.

    maehl@DESKTOP-KFT9U41 MINGW64 /d/Pokemmo/pokemmo/data/strings
    $ help pwd
    pwd: pwd [-LPW]
        Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links
      -W        print the Win32 value of the physical directory

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.


# Questions
### 1.
What should be outputted to the display when you type echo Hello World?

### 2.
How do I find what directory you are currently in?

### 3.
If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?

### 4.
What command would you use to see hidden files?

### 5.
How do you create a file called myfile?

### 6.
What command can you use to find the file type of a file?

### 7.
What's a good way to see the contents of a file?

### 8.
How do you quit out of a less command?

### 9.
What is the command to clear the terminal?

### 10.
What flag do you need to specify to copy over a directory?

### 11.
How do you rename a file called cat to dog?

### 12.
What command is use to make a directory?

### 13.
How do you removbe a file called myfile?

### 14.
What option should I specify for find if I want to search by name?

### 15.
How do you get quick command line help for built-in bash commands?

# Answers
### 1.
Hello World

### 2.
    $ pwd

### 3.
cd ..

### 4.
    $ ls -a

### 5.
    $ touch myfile

### 6.
    $ file

### 7.
cat

### 8.
q

### 9.
    $ clear

### 10.
-r

### 11.
    $ mv cat dog

### 12.
    $ mkdir

### 13.
    $ rm myfile

### 14.
-name

### 15.
