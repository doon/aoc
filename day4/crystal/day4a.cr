require "set"

valid = 0

File.each_line("../input/input.txt") do |line|
        words = line.strip().split()
        valid += 1 if words.to_set.size == words.size
end

puts "Valid: #{valid}"
