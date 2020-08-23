

object ScalaPractice1 {
  // write the code for the Fibonacci sequence
   var prev2 = 0                            
   var prev1 = 1                                  
	 for (x <- 1 to 10) {
	 	  var Fib = prev1 + prev2
	 	  prev2 = prev1
	 	  prev1 = Fib
	 	  println(Fib)
	 }      
}