local nvim_banners = {}
local banners = {}
local width_devider

function nvim_banners.setup(config)
    if config["banners"] then
        banners = config["banners"]
    else
        banners = require("nvim_banners.banners")
    end

    if config["width_devider"] then
        width_devider = config["width_devider"]
    else
        width_devider = 5
    end

end

function nvim_banners.get_random()
    math.randomseed(os.clock())
    local width = vim.api.nvim_win_get_width(0)
    local length = banners["length"]
    local banner = {}
    local number = 0
    local size = width + 1
    local count = 0

    while (size > width or size < width / width_devider and count) do
        number = math.random(length)
        size = banners[number]["size"] + 10
        count = count + 1

        if count > length * 2 then
            break
        end
    end

    banner = banners[number]["banner"]
    return banner
end

return nvim_banners
