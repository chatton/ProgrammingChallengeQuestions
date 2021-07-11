package kata

func HasUniqueChar(str string) bool {
	counts := make(map[rune]bool)
	for _, char := range str {
		if ok, _ := counts[char]; ok {
			return false
		} else {
			counts[char] = true
		}
	}
	return true
}
