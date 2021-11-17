export abstract class Comparator<T> {
  abstract compare(array: T[], idx1: number, idx2: number): boolean;
}

export class LessThan extends Comparator<number> {
  compare(array: number[], idx1: number, idx2: number): boolean {
    return array[idx1] < array[idx2];
  }
}

export class GreaterThan extends Comparator<number> {
  compare(array: number[], idx1: number, idx2: number): boolean {
    return array[idx1] > array[idx2];
  }
}

export class EqualTo extends Comparator<number> {
  compare(array: number[], idx1: number, idx2: number): boolean {
    return array[idx1] === array[idx2];
  }
}
