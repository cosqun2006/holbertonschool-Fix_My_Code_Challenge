# Filter only integer arguments, convert them to integers, sort, and print
result = ARGV.select { |arg| arg =~ /^-?\d+$/ }
             .map(&:to_i)
             .sort

puts result
