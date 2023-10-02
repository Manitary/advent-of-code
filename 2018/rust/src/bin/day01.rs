use std::collections::HashSet;
use std::error::Error;
use std::fs;

pub fn main() -> Result<(), Box<dyn Error>> {
    let input: Vec<isize> = fs::read_to_string("input/day01.txt")
        .unwrap()
        .lines()
        .map(|n: &str| n.parse::<isize>().unwrap())
        .collect();
    println!("Part 1: {}", part_1(&input));
    println!("Part 2: {}", part_2(&input));
    Ok(())
}

pub fn part_1(input: &Vec<isize>) -> isize {
    input.iter().sum()
}

pub fn part_2(input: &Vec<isize>) -> isize {
    let mut freqs: HashSet<isize> = HashSet::new();
    let mut freq: isize = 0;
    freqs.insert(freq);
    for x in input.iter().cycle() {
        freq += x;
        if freqs.contains(&freq) {
            break;
        }
        freqs.insert(freq);
    }
    freq
}
