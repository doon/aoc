valid = 0

File.each_line("../input/input.txt") do |line|
  isValid = true
  line.split.each_combination(2) do |a|
    perms = a[1].chars.permutations.map {|b| b.join }
    if perms.includes? a[0]
      isValid = false
      break
    end
  end
  valid += 1 if isValid
end

puts "Valid: #{valid}"
