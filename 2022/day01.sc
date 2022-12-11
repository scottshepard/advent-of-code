import scala.io.Source

val lines = Source.fromFile("inputs/day01.txt").getLines.toList

// Perhaps not the most functional in style, but it works
def splitFile(lines: List[String]): List[List[Int]] = {
    var lines2 = lines
    var i = lines2.indexOf("")
    var j = 0
    var output = List[List[Int]]()
    while (i > 0) {
        val newLines = lines2.splitAt(i)
        output = newLines(0).map(_.toInt) :: output
        lines2 = newLines(1).drop(1)
        i = lines2.indexOf("")
        j += 1
    }
    output
}

val elves = splitFile(lines).map(_.sum)
println(s"Part 1: ${elves.max}")

// Couldn't figure out how to inverse sort, so taking from the end of a sorted list instead
println(s"Part 2: ${elves.sorted.takeRight(3).sum}")


