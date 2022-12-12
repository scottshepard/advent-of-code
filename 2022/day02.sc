import scala.io.Source


def playRound1(players: Array[String]): Int = {
  val p1 = players(0)
  val p2 = players(1)
  if (p1 == "A") {
    if (p2 == "X")      3 + 1
    else if (p2 == "Y") 6 + 2
    else if (p2 == "Z") 0 + 3
    else                0
  } else if (p1 == "B") {
    if (p2 == "X")      0 + 1
    else if (p2 == "Y") 3 + 2
    else if (p2 == "Z") 6 + 3
    else                0
  }
  else if (p1 == "C") {
    if (p2 == "X")      6 + 1
    else if (p2 == "Y") 0 + 2
    else if (p2 == "Z") 3 + 3
    else                0
  } else {
    0
  }
}

def playRound2(players: Array[String]): Int = {
  val p1 = players(0)
  val p2 = players(1)
  if (p1 == "A") {
    if (p2 == "X")      0 + 3
    else if (p2 == "Y") 3 + 1
    else if (p2 == "Z") 6 + 2
    else                0
  } else if (p1 == "B") {
    if (p2 == "X")      0 + 1
    else if (p2 == "Y") 3 + 2
    else if (p2 == "Z") 6 + 3
    else                0
  }
  else if (p1 == "C") {
    if (p2 == "X")      0 + 2
    else if (p2 == "Y") 3 + 3
    else if (p2 == "Z") 6 + 1
    else                0
  } else {
    0
  }
}

val lines = Source.fromFile("inputs/day02.txt").getLines.toList

val scores1 = lines.map(_.split(" ")).map(playRound1(_))
println(s"Part 1: ${scores1.sum}")

val scores2 = lines.map(_.split(" ")).map(playRound2(_))
println(s"Part 2: ${scores2.sum}")
