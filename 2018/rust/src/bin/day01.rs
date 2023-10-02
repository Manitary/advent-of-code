use std::collections::HashSet;
use std::error::Error;
use std::fs;

pub fn main() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("input/day01.txt")?;
    println!("Part 1: {}", part_1(&input));
    println!("Part 2: {}", part_2(&input));
    Ok(())
}

pub fn part_1(input: &str) -> isize {
    input
        .lines()
        .into_iter()
        .map(|n: &str| n.parse::<isize>().unwrap())
        .sum()
}

pub fn part_2(input: &str) -> isize {
    let mut freqs: HashSet<isize> = HashSet::new();
    let mut freq: isize = 0;
    freqs.insert(freq);
    for x in input
        .lines()
        .into_iter()
        .cycle()
        .map(|n: &str| n.parse::<isize>().unwrap())
    {
        freq += x;
        if freqs.contains(&freq) {
            break;
        }
        freqs.insert(freq);
    }
    freq
}
