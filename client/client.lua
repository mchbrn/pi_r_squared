local arg = {...}
arg = table.concat(arg, ",")
print(arg)
--[[for i = 1, 1, #arg do
	arg[i]
]]
-- Get parameters
--[[local prmt = {...}
local prmtErr = "Three parameters must be given in the form: 'todo item', YYYY-MM-DD, true/false"
local delimiter = string.sub(prmt[2], 5, 5)
if #prmt ~= 3 or (prmt[3] ~= "true" and prmt[3] ~= "false") --[[or parsedQuery is wrong]]--[[then 
	error(prmtErr) 
end

print(type(prmt[1]))


--[[
if pcall(parse) then
	print("No errors")
else
	print("Oh no! An error!")
end
]]
-- local status, err = pcall(parse() error() end)


	

-- load namespace
local socket = require("socket")
-- create a TCP socket and bind it to the local host, at any port
local client = assert(socket.tcp())
-- local client = assert(socket.bind("*", 0))
-- find out which port the OS chose for us
-- local ip, port = client:getsockname()

local err, line = client:connect("100.73.120.110", 39359)
print(err, line)
client:send(arg .. "\n")

