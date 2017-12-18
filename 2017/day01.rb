if ARGV.length > 0
  input = ARGV[0]
else
  input = File.read('inputs/day01.txt')
end

def checksum(num)
  sum = 0
  digits = num.split('')
  fulldigits = digits + digits
  for i in 0...digits.length
    if(digits[i] == fulldigits[i+1])
      sum += digits[i].to_i
    end
  end
  sum
end

puts checksum(input)
