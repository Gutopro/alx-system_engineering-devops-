#!/usr/bin/env ruby

# Accept the argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /School/

# Pass the input to the regular expression matching method
result = pattern.match(input)

# Print the result
if result
  puts result[0]
else
  puts ""
end

