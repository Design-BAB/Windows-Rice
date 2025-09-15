package main

import "fmt"

func main() {
	// Define colors
	red := "\033[38;2;255;51;102m" // I ended up using a different red (#ff3366)
	green := "\033[38;5;47m"
	blue := "\033[38;5;32m"
	yellow := "\033[38;5;220m"
	reset := "\033[0m"
	// Print with colors
	fmt.Println(red + "          ^!!                                                 ")
	fmt.Println("          ^~^                                                  ")
	fmt.Println("              !??7                                             ")
	fmt.Println("       .!7!   :::  !?777.                                      ")
	fmt.Println("       .::.       :!!!!: !7777:      :7777777!!!:             ")
	fmt.Println("           :???~        !????~      :?JJJJJJJJJ?.   " + green + "^7~^:.    ")
	fmt.Println(red + "           .... ^?JJJ^             .?J???????J?:   " + green + "^777?77!^. ")
	fmt.Println(red + "                ^~~~^ ~J??J!       7J???????J?:   " + green + ":77777777?7~")
	fmt.Println(blue + "   .::              " + red + ":!!!!!.       !JJJJ????JJ^   " + green + ":77777777777:")
	fmt.Println(blue + "  .7?7                           " + red + "!JJJJJJJJJJ~   " + green + ".77777777777^ ")
	fmt.Println(blue + "       ~~~~                      " + red + ":::::^^~~!~   " + green + ".7?77777777?^  ")
	fmt.Println(blue + ".^^:  :777^ ^~~~^                              " + green + ".~!77?7777?~   ")
	fmt.Println(blue + "^77:       ~JJJJ^.^^^~~.      ^??????77!!:         " + green + ".^!7??!    ")
	fmt.Println(blue + "    ^???^        ?YYYY!      :JYYYYYYYYYJ.   " + yellow + ":^^:.    " + green + ".^~     ")
	fmt.Println(blue + "    ^~~^ ^?777:             .?YJJJJJJJYJ:   " + yellow + ":~~~~~~^:         ")
	fmt.Println(blue + "        .7???! ~7!!7^      .?YJJJJJJJYJ:   " + yellow + ":~~~~~~~~~~:       ")
	fmt.Println(blue + "              ^YYYY?.      7YJJJJJJJYY^   " + yellow + ".~~~~~~~~~~~:       ")
	fmt.Println(blue + "              ....:.      7YYYYYYYYYY~   " + yellow + ".~~~~~~~~~~~:        ")
	fmt.Println(blue + "                         .~~~~!!77?J!   " + yellow + ".~~~~~~~~~~~^         ")
	fmt.Println(blue + "                                        " + yellow + ":~~~~~~~~~~^          ")
	fmt.Println(blue + "                                          " + yellow + "..:^~~~~^           ")
	fmt.Println(blue + "                                                " + yellow + "^~	    " + reset)
}
