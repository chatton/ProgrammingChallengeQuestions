/*

Description:
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

*/
func FindUniq(arr []float32) float32 {
  counts := make(map[float32]int)

  for _, f := range arr {
    if val, ok := counts[f]; ok {
      counts[f] = val + 1
    } else {
      counts[f] = 1
    }
  }

  for _, f := range arr {
    if val, _ := counts[f]; val == 1 {
        return f
    }
  }
  
  return -1 // should never get here
}