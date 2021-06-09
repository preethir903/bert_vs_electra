import _pickle as cPickle
import pickle
import treeUtil
import pandas as pd
import pathlib

def extract_root_sentence_label(ideology_lib): 
    '''
    Extract root node and label
    '''
    label = []
    sentence = []
    for ex_tree in ideology_lib: 
        counter = 0
        while counter < 1: 
            for node in ex_tree: 
                counter += 1
                if hasattr(node, 'label') and 'ROOT' in node.pos:
                    label.append(node.label)
                    sentence.append(node.get_words())
    return label, sentence

def create_df_label_sentence(ideology_lib): 
    """
    Extract label / sentence; return as DataFrame
    """
    label, sentence = extract_root_sentence_label(ideology_lib)
    return pd.DataFrame(zip(label, sentence), columns = ['ideology', 'sentence'])


def create_sentence_label_full_df():
    """
    Extract label / sentence from liberal and conservative
    Sample liberal 
    """
    [lib, con, neutral] = pickle.load(open( pathlib.Path(__file__).parent / 'ibc_data_full.pkl', 'rb'))
    lib_df = create_df_label_sentence(lib)
    con_df = create_df_label_sentence(con)
    frac = len(con_df) / len(lib_df)
    lib_df = lib_df.sample(frac=frac,random_state=1).copy()
    return pd.concat([lib_df, con_df]).reset_index(drop=True)
