nums = rand(1000)

function relu(x)
	if x > 0
		return x
	else
		return 0
	end
end


function sigmoid(x)
	out = 1/(1+exp(-x))
	return out
end

function neuron(X, W, B)
	return tanh(sum(X.*W .+ B))
end


function looping(iterations)
	for i in 0:1:iterations
		relu(i)
		tanh(i)
		sigmoid(i)
		neuron(nums, nums, nums)
	end
end

looping(1)

@time looping(1000000)