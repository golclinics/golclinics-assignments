import { Person } from "./assignment-1";

export abstract class Comparator<T> {
  abstract compare(
    array: T[],
    idx1: number,
    idx2: number,
    prop: string
  ): boolean;
}

export class LessThan<Person> {
  compare(array: Person[], idx1: number, idx2: number, prop: string): boolean {
    return array[idx1][prop] < array[idx2][prop];
  }
}

export class GreaterThan<Person> {
  compare(array: Person[], idx1: number, idx2: number, prop: string): boolean {
    return array[idx1][prop] > array[idx2][prop];
  }
}
