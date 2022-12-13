import scala.io.Source

val input = Source.fromFile("inputs/day04.txt").getLines.toList.map(_.split(","))

def fullyOverlap(elves: Array[String]): Boolean = {
  val e1 = elves(0).split("-").map(_.toInt)
  val e2 = elves(1).split("-").map(_.toInt)

  (e1(0) <= e2(0) && e1(1) >= e2(1)) || (e2(0) <= e1(0) && e2(1) >= e1(1))
}

def partiallyOverlap(elves: Array[String]): Boolean = {
  val e1 = elves(0).split("-").map(_.toInt)
  val e2 = elves(1).split("-").map(_.toInt)

  (
    (e1(0) <= e2(0) && e1(1) >= e2(0))
      || (e1(0) <= e2(0) && e1(1) >= e2(1))
      || (e2(0) <= e1(0) && e2(1) >= e1(0))
      || (e2(0) <= e1(0) && e2(1) >= e1(1))
    )
}

println(s"Part 1: ${input.map(fullyOverlap).filter(x => x).length}")
println(s"Part 2: ${input.map(partiallyOverlap).filter(x => x).length}")
