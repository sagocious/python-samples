// GCD Function
fn gcd(m: i32, n: i32) -> i32 {
   if m == 0 {
      n.abs()
   } else {
      gcd(n % m, m)
   }
}

// Test
fn main(){
	println!("{}", gcd(12, 18));
}