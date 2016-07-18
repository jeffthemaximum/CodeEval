require 'pry'

line = "5 4 9 10 7 3 2 1 6 | 1"
lines = line.split(" | ")
arr = lines[0].split(" ").map{|e| e.to_i}
it = lines[1].to_i
count = 0
while count < it

  endpoint = arr.length-(count-1)
  arr[count...endpoint].each_with_index do |el,idx|
    if arr[idx+1] != nil && arr[idx] > arr[idx+1]
      arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    end
  end

  arr = arr.reverse

  arr[count...endpoint].each_with_index do |el,idx|
    if arr[idx+1] != nil && arr[idx] < arr[idx+1]
      arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    end
  end

  arr = arr.reverse

  count += 1

end
arr.each_with_index do |el,idx|
  if idx == arr.length - 1
    print el.to_s + "\n"
  else
    print el.to_s + " "
  end
end

