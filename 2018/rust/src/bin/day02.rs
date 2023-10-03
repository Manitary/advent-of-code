use itertools::Itertools;
use std::collections::HashMap;
use std::error::Error;
use std::fs;

pub fn main() -> Result<(), Box<dyn Error>> {
    let input: Vec<String> = fs::read_to_string("input/day02.txt")
        .unwrap()
        .lines()
        .map(|line| line.to_string())
        .collect();
    println!("Part 1: {}", part_1(&input));
    println!("Part 2: {}", part_2(&input).unwrap());
    Ok(())
}

pub fn part_1(input: &Vec<String>) -> isize {
    let mut two = 0;
    let mut three = 0;
    for word in input {
        let freq = word.chars().fold(HashMap::new(), |mut counter, c| {
            *counter.entry(c).or_insert(0) += 1;
            counter
        });
        two += if freq.values().any(|v| v == &2) { 1 } else { 0 };
        three += if freq.values().any(|v| v == &3) { 1 } else { 0 };
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
