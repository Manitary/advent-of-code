use aocd::*;
use std::collections::HashSet;

#[aocd(2018, 1)]
pub fn main() {
    let input: Vec<isize> = input!()
        .lines()
        .map(|n: &str| n.parse::<isize>().unwrap())
        .collect();
    submit!(1, part_1(&input));
    submit!(2, part_2(&input));
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
