import string
import argparse
import os
parser = argparse.ArgumentParser(description='Process some integers.')

# common
parser.add_argument('--num_classes',        default=2,       required=True,  type=int)
parser.add_argument('--batch_size',         default=32,      required=False, type=int)
parser.add_argument('--num_steps',          default=12000,   required=False, type=int)
parser.add_argument('--crop_height',        default=300,     required=True,  type=int)
parser.add_argument('--crop_width',         default=300,     required=True,  type=int)
parser.add_argument('--train_num_examples', default=300,     required=True,  type=int)
parser.add_argument('--eval_num_examples',  default=300,     required=True,  type=int)
parser.add_argument('--eval_height',        default=300,     required=True,  type=int)
parser.add_argument('--eval_width',         default=300,     required=True,  type=int)
parser.add_argument('--train_input_path',   default=300,     required=True,  type=str)
parser.add_argument('--eval_input_path',    default=300,     required=True,  type=str)

## 2nd stage
parser.add_argument('--filter_scale',         default=0,     required=True,  type=float)
#parser.add_argument('--fine_tune_checkpoint', default=None,  required=True,  type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    context = vars(args)
    context['fine_tune_checkpoint'] = f'STAGE1/icnet_{args.crop_width:04d}x{args.crop_height:04d}_{args.filter_scale:02.2f}/comp/pruned_model.ckpt'


    DIR_FOR_1ST_STAGE = os.path.join('TRAIN_CONF','1st_stage')
    DIR_FOR_2ND_STAGE = os.path.join('TRAIN_CONF','2nd_stage')
    DIR_FOR_CMD       = 'EXEC_CMDS'

    CONF_NAME_FOR_1ST_STAGE = f'icnet_1st_{args.crop_width:04d}x{args.crop_height:04d}_{args.filter_scale:02.2f}.conf'
    CONF_NAME_FOR_2ND_STAGE = f'icnet_2nd_{args.crop_width:04d}x{args.crop_height:04d}_{args.filter_scale:02.2f}.conf'
    CMD_NAME                = f'cmds_for_{args.crop_width:04d}x{args.crop_height:04d}_{args.filter_scale:02.2f}.txt'

    CONF_PATH_FOR_1ST_STAGE = os.path.join(DIR_FOR_1ST_STAGE, CONF_NAME_FOR_1ST_STAGE)
    CONF_PATH_FOR_2ND_STAGE = os.path.join(DIR_FOR_2ND_STAGE, CONF_NAME_FOR_2ND_STAGE)
    CMD_PATH                = os.path.join(DIR_FOR_CMD, CMD_NAME)
    
    print(CONF_PATH_FOR_1ST_STAGE)
    print(CONF_PATH_FOR_2ND_STAGE)
    print(CMD_PATH)
    
    # for 1st stage
    with open(os.path.join(DIR_FOR_1ST_STAGE, 'template.conf')) as f:
        temp = f.read()
    template = string.Template(temp)
    conf     = template.substitute(context)
    with open(CONF_PATH_FOR_1ST_STAGE, 'w') as f:
        f.write(conf)

    # for 2nd stage
    with open(os.path.join(DIR_FOR_2ND_STAGE, 'template.conf')) as f:
        temp = f.read()
    template = string.Template(temp)
    conf     = template.substitute(context)
    with open(CONF_PATH_FOR_2ND_STAGE, 'w') as f:
        f.write(conf)

    # for cmds
    with open(os.path.join(DIR_FOR_CMD,'template.txt')) as f:
        temp = f.read()
    template = string.Template(temp)
    context={
        'stage1_config': CONF_PATH_FOR_1ST_STAGE,
        'train_tag'    : f'icnet_{args.crop_width:04d}x{args.crop_height:04d}_{args.filter_scale:02.2f}',
        'shape'        : f'-1,{args.crop_width},{args.crop_height},3',
        'num_steps'    : f'{args.num_steps}',
        'filter_scale' : f'{args.filter_scale}',
        'stage2_config': CONF_PATH_FOR_2ND_STAGE,
    }
    cmd      = template.substitute(context)    
    with open(CMD_PATH, 'w') as f:
        f.write(cmd)
                     

        
