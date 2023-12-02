use aocd::*;
use itertools::Itertools;
use std::error::Error;

#[aocd(2018, 2)]
pub fn main() {
    let input: Vec<String> = input!().lines().map(|line| line.to_string()).collect();
    submit!(1, part_1(&input));
    submit!(2, part_2(&input).unwrap());
}

pub fn part_1(input: &Vec<String>) -> isize {
    let mut two = 0;
    let mut three = 0;
    for word in input {
        let freq = word.chars().fold([0u8; 26], |mut counter, c| {
            counter[c as usize - 'a' as usize] += 1;
            counter
        });
        if freq.contains(&2) {
            two += 1
        };
        if freq.contains(&3) {
            three += 1
        };
    }
    two * three
}

pub fn part_2(input: &Vec<String>) -> Result<String, Box<dyn Error>> {
    for (w1, w2) in input.iter().tuple_combinations() {
        let mut diff = 0;
        let mut idx = 0;
        for (i, (c1, c2)) in w1.chars().zip(w2.chars()).enumerate() {
            if c1 == c2 {
                continue;
            }
            diff += 1;
            if diff > 1 {
                break;
            }
            idx = i;
        }
        if diff == 1 {
            let mut result = w1.clone();
            result.replace_range(idx..idx + 1, "");
            return Ok(result);
        }
    }
    panic!("No solution found")
}
