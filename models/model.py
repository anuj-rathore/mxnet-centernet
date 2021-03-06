from models.hourglass import get_hourglass_net
from models.resnet import get_pose_net

_model_factory = {
    'hourglass': get_hourglass_net,
    'res': get_pose_net,
}


def create_model(arch, heads, head_conv_channels, ctx):
    ind = arch.find('_')
    num_layers = int(arch[ind+1:]) if '_' in arch else 0
    arch = arch[:ind] if '_' in arch else arch

    get_model_func = _model_factory[arch]
    model = get_model_func(num_layers=num_layers, heads=heads, head_conv=head_conv_channels, ctx = ctx)
    return model

def load_model(model, model_load_path, ctx):
    model.load_parameters(model_load_path, ctx=ctx, ignore_extra=True, allow_missing = True)
    return model

def save_model(model, model_save_path):
    model.save_parameters(model_save_path)
