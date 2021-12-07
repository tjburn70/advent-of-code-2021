import * as fs from 'fs'
import * as readline from 'readline'

function main() {
  const lines = readInput()
  const oxygenRating = determineRating(lines, 0, '1', determineMaxOccurence)
  const c02ScrubberRating = determineRating(lines, 0, '0', determineMinOccurence)

  console.log("oxygenRating", oxygenRating)
  console.log("c02ScrubberRating", c02ScrubberRating)
  const answer = parseInt(oxygenRating, 2) * parseInt(c02ScrubberRating, 2)
  console.log("answer", answer)
}

function readInput(): string[] {
  return fs.readFileSync('./day3-input.txt')
   .toString()
   .split('\n');
}

function determineRating(lines: string[], charIndex: number, tieGoesTo: string, callback: Function): any {
  const bitOccurence = callback(
    lines,
    charIndex,
    tieGoesTo
  )
  const filteredLines = lines.filter((bitSequence) => bitSequence.charAt(charIndex) === bitOccurence.toString())
  if (filteredLines.length === 1) {
    return filteredLines[0]
  }

  return determineRating(filteredLines, charIndex + 1, tieGoesTo, callback)
}

function determineMaxOccurence(lines: string[], charIndex: number, tieGoesTo: string): string {
  const bitToOccurences = bitsByOccurence(lines, charIndex)
  if (bitToOccurences['1'] == bitToOccurences['0']) {
    return tieGoesTo
  }

  return bitToOccurences['1'] > bitToOccurences['0'] ? '1': '0'
}

function determineMinOccurence(lines: string[], charIndex: number, tieGoesTo: string): string {
  const bitToOccurences = bitsByOccurence(lines, charIndex)
  if (bitToOccurences['1'] == bitToOccurences['0']) {
    return tieGoesTo
  }

  return bitToOccurences['1'] < bitToOccurences['0'] ? '1': '0'
}

function bitsByOccurence(lines: string[], charIndex: number): Record<string, number> {
  const bitToOccurences: Record<string, number> = {}
  for (const line of lines) {
    const bit = line.charAt(charIndex)
    if (bit in bitToOccurences) {
      bitToOccurences[bit]++
    } else {
      bitToOccurences[bit] = 0
    }
  }
  return bitToOccurences
}

main()
