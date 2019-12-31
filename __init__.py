bl_info = {
    "name": "Pallini_Tools",
    "author": "ぱりーに（pallini）",
    "version": (0, 1),
    "blender": (2, 81, 1),
    "location": "3Dビューポート > Pallini_Tools ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Tools"
}


if "bpy" in locals():
    import imp
    imp.reload(pal_SetResolutionFromBG)
else:
    from .modules import pal_SetResolutionFromBG


import bpy


# Blenderに登録するクラス
classes = [
    pal_SetResolutionFromBG.PalliniTools_OT_SetResolutionFromBG,
    pal_SetResolutionFromBG.PalliniTools_PT_CustomPanel,
]


# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)


# アドオン無効化時の処理
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


# メイン処理
if __name__ == "__main__":
    register()