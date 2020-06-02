import { Equalable } from './equalable'

export function findByEquality<T extends Equalable<T>>(
  array: Array<T>,
  itemToFind: T
): T {
  array.forEach(item => {
    if (item.equals(itemToFind)) {
      return item
    }
  })

  return null
}

export function findIndexByEquality<T extends Equalable<T>>(
  array: Array<T>,
  itemToFind: T
): number {
  for (let i = 0; i < array.length; i++) {
    if (array[i].equals(itemToFind)) {
      return i
    }
  }

  return -1
}
