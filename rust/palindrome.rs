// Is palindrome
fn is_palindrome(string: &str) -> bool {
    let half_len = string.len()/2;
    string.chars().take(half_len).eq(string.chars().rev().take(half_len))
}

// Test
fn main(){
	println!("{}", is_palindrome("12321"));
}