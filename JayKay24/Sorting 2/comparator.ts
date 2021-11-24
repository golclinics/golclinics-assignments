import { Person } from "./assignment-1";

export abstract class Comparator {
  // If array[prop] is a string, compare the UTF-16 code values
  abstract compare(
    array: Person[],
    idx1: number,
    idx2: number,
    prop: string
  ): boolean;
}

export class LessThan {
  compare(array: Person[], idx1: number, idx2: number, prop: string): boolean {
    return array[idx1][prop] < array[idx2][prop];
  }
}

export class GreaterThan {
  compare(array: Person[], idx1: number, idx2: number, prop: string): boolean {
    return array[idx1][prop] > array[idx2][prop];
  }
}
