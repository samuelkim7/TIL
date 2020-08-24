### Concepts
- A Shell is a command-line interpreter and typical operations performed by shell scripts include file manipulation, program execution, and printing text.
- A Shell gathers input from you and executes programs based on that input.
- Shell Prompt: The prompt, $, which is called the command prompt, is issued by the shell. While the prompt is displayed, you can type a command.
- Shell Scripts: a shell script is a list of commands, which are listed in the order of execution.

### Basics of Script

- (in a script file) #!/bin/sh : This tells the system that the commands that follow are to be executed by the Bourne shell.
- $ chmod +x test.sh : This command makes the script executable

$ vi test.sh
```shell
#!/bin/sh
pwd
ls
```

#### Variable
- Variable Names: The name of a variable can contain only letters (a to z or A to Z), numbers (0 to 9) or the underscore character (_).
- Defining variable: variable_name=variable_value
- Accessing Values: $variable_value
- Special variables
  - $0: Filename of the current script
  - $n: These variables correspond to the arguments with which a script was invoked.
  - $@: All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.
  - $$: The process number of the current shell
 
$ vi test.sh
```shell
#!/bin/sh

for TOKEN in $*
do
   echo $TOKEN
done
```
$ sh test.sh
```shell
$./test.sh Zara Ali 10 Years Old
Zara
Ali
10
Years
Old
```

#### Array
```shell
#!/bin/sh
#Defining an array
NAME=(Sam Kim Myeongwon)
#Accessing array values
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
```
```shell
$./test.sh
First Index: Sam
Second Index: Kim
```
#### Operators
- Bourne shell didn't originally have any mechanism to perform simple arithmetic operations but it uses external programs, either awk or **expr**.
- basic format: `expr `
- There must be spaces between operators and expressions. 2+2 is not correct. It should be 2 + 2.
- Multiplication: \*
```shell
Live Demo
#!/bin/sh
val=`expr 2 + 2`
echo "Total value : $val"
```
```shell
Total value : 4
```
- Relational Operators
  - -eq: ==
  - -ne: !=
  - -gt: >
  - -lt: <
  - -ge: >=
  - -le: <=
- File Test Operators
  - -f file: Checks if file is an ordinary file as opposed to a directory or special file.
  - -x file: Checks if file is executable.
  - -e file: Checks if file exists
