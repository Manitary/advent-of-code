use aocd::*;
use itertools::enumerate;
use ndarray::{s, Array2, ArrayBase, Dim, OwnedRepr};
use regex::Regex;

#[aocd(2018, 3)]
pub fn main() {
    let input = input!();
    let rectangles: Vec<[usize; 4]> = parse_input(input);
    let grid = make_grid(&rectangles);
    submit!(1, part_1(&grid));
    submit!(2, part_2(&grid, &rectangles));
}

fn parse_input(input: String) -> Vec<[usize; 4]> {
    let re = Regex::new(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)").unwrap();
    re.captures_iter(&input)
        .map(|m| {
            m.iter()
                .skip(1)
                .map(|r| r.unwrap().as_str().parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
                .try_into()
                .unwrap()
        })
        .collect()
}

fn make_grid(rectangles: &Vec<[usize; 4]>) -> ArrayBase<OwnedRepr<i32>, Dim<[usize; 2]>> {
    let mut grid = Array2::zeros((1000, 1000));
    for r in rectangles {
        grid.slice_mut(s![r[0]..r[0] + r[2], r[1]..r[1] + r[3]])
            .scaled_add(1, &Array2::ones((r[2], r[3])))
    }
    grid
}

pub fn part_1(grid: &ArrayBase<OwnedRepr<i32>, Dim<[usize; 2]>>) -> usize {
    grid.fold(0, |mut acc, c| {
        if *c > 1 {
            acc += 1
        };
        acc
    })
}

pub fn part_2(
    grid: &ArrayBase<OwnedRepr<i32>, Dim<[usize; 2]>>,
    rectangles: &Vec<[usize; 4]>,
) -> usize {
    'r: for (i, r) in enumerate(rectangles) {
        for x in grid.slice(s![r[0]..r[0] + r[2], r[1]..r[1] + r[3]]).iter() {
            if *x > 1 {
                continue 'r;
            }
        }
        return i + 1;
    }
    panic!("No valid rectangle found.")
}
