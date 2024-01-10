#!/usr/bin/env ruby
# Regex match for school

# Check if an argument is provided
if ARGV.length == 1
  # Use scan with the regular expression to find occurrences of the word "School"
  result = ARGV[0].scan(/\bSchool\b)

  # Check if there are any matches
  if result.empty?
    puts "No match found."
  else
    # Print the matched word(s)
    puts result.join
  end
else
  puts "Please provide exactly one argument."
end
