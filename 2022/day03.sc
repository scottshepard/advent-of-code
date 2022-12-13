import scala.io.Source

val input = Source.fromFile("inputs/day03.txt").getLines.toList

def similiarItems(rucksack: String): Char = {
  val compartments = rucksack.splitAt(rucksack.length / 2)

  compartments(0).intersect(compartments(1)).distinct(0)
}

def findBadge(group: List[String]): Char = {
  group(0).intersect(group(1)).intersect(group(2)).distinct(0)
}

def prioritize(char: Char): Int = {
  val letters = 'a' to 'z'

  var bonus = 0
  val newChar = if (char.isUpper) {
    bonus = 27
    char.toString.toLowerCase()(0)
  } else {
    bonus = 1
    char
  }

  letters.indexOf(newChar) + bonus
}

val overlaps = input.map(similiarItems(_))
println(s"Part 1: ${overlaps.map(prioritize(_)).sum}")

println(s"Part 2: ${input.grouped(3).toList.map(findBadge(_)).map(prioritize(_)).sum}")