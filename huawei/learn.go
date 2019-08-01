package main

import "fmt"

func main() {
	var a = 100
	var b = 200
	var ret int
	ret = max(a, b)
	fmt.Println("最大值是: %d\n", ret)
          var getmin = func(x, y int) int {
		if x > y {
	            return y
		}
		else{
		return x 
	          }
	            
		
	}
          fmt.Println("最小值为: %d\n", getmin(2,3))


}

func max(a, b int) int {
	var result int
	if a > b {
		result = a
	} else {
		result = b
	}
	return result
}


