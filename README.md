# Banners.nvim

**banners.nvim** is a pluging that gets a random banner each time you open NeoVim

## Install

Install with your preferred package manager:

[vim-plug](https://github.com/junegunn/vim-plug)
```vim
Plug 'eduhcs/banners.nvim'
```

[packer](https://github.com/wbthomason/packer.nvim)
```lua
use 'eduhcs/banners.nvim'
```
## Generanting the banners file

To generate the [asii-banners.lua](/lua/asii-banners.lua) file:
```bash
python3 gen-banners.py
```

## Setup with [alpha-nvim](https://github.com/goolord/alpha-nvim)

To configure **banners.nvim** you just need to put this into your alpha-nvim configuration and replace **<theme-name>** with the theme that you are using

```lua
-- import and setup
local nvim_banners = require("nvim_banners")
nvim_banners.setup({
    -- banners = {"123","456","789"}, -- to use your own banners
    -- width_devider = 5, -- controls the center of the banner
})

-- Set header for the startify theme
<theme-name>.section.header.val = nvim_banners.get_random()

-- set the highlighting type to String
<theme-name>.section.header.opts = {
    hl = "String",
}
```
