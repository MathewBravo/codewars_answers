fn is_palindrome(s: String) -> bool {
    let mut working_string: String = String::from(" ");
    for char in s.to_lowercase().chars() {
        if char.is_alphanumeric() {
            working_string.push(char)
        }
    }
    let reverse_working_string = working_string.chars().rev().collect::<String>();

    working_string.trim() == reverse_working_string.trim()
}

fn main() {
    println!("{}", is_palindrome(String::from("0P")));
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_is_palindrome() {
        let test1 = String::from("A man, a plan, a canal: Panama");
        let test2 = String::from("race a car");
        assert_eq!(is_palindrome(String::from("0P")), true);
        assert_ne!(is_palindrome(test2), true);
    }
}
