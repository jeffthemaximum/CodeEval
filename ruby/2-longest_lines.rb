=begin
 Sample code to read in test cases:
File.open(ARGV[0]).each_line do |line,index|
  
end
=end
require 'pry'


test = [2, "Hello World", "CodeEval", "Quick Fox", "A", "San Francisco"]
biggest = []
test.each do |line|
  biggest.push(line)
end

output_count = biggest.shift.to_i
biggest = biggest.sort_by{|x| x.length}.reverse[0...output_count]

puts biggest