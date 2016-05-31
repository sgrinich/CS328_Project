import object_loader
import numpy
import similarity 

object_names = object_loader.load_name_data("data/classes.txt")
feature_matrix = object_loader.load_object_feature_data("data/predicate-matrix-binary-above-25-percent.txt")
feature_names = object_loader.load_name_data("data/predicates.txt")

def getobjectIndexFromName(name, object_names):
    i = 0
    while object_names[i] != name:
        i += 1

        if i > (len(object_names) - 1):
            return None
    return i

def getFeatureIndexFromName(feature, object_features):
    i = 0
    while object_features[i] != feature:
        i += 1

        if i > (len(object_features) - 1):
            return None
    return i

def get_model_similarities(person):

    # replace the below string parameter to see top things similar to it according to each model
    character_index = getobjectIndexFromName(person, object_names)
    ottter_binary_features = feature_matrix[character_index]

    tversky_similarities = []
    shepard_similarities = []
    medin_similarities = []


    for object_index in range(len(feature_matrix)):
        if object_index == character_index:
            continue
        else:
            tversky_similarity = similarity.get_tversky_similarity(feature_matrix[character_index], feature_matrix[object_index])
            shepard_similarity = similarity.get_shepard_similarity(feature_matrix[character_index], feature_matrix[object_index])
            medin_similarity = similarity.get_medin_similarity(feature_matrix[character_index], feature_matrix[object_index])

            tversky_similarities.append((object_names[object_index], tversky_similarity))
            shepard_similarities.append((object_names[object_index], shepard_similarity))
            medin_similarities.append((object_names[object_index], medin_similarity))
            
    top_tversky = sorted(tversky_similarities, key=lambda x: x[1])
    top_tversky.reverse()

    top_shepard = sorted(shepard_similarities, key=lambda x: x[1])
    top_shepard.reverse()

    top_medin = sorted(medin_similarities, key=lambda x: x[1])
    top_medin.reverse()



    tversky_ascending = []
    for i in range(len(top_tversky)):
        tversky_ascending.append(top_tversky[i][0])

    shepard_ascending = []
    for i in range(len(top_shepard)):
        shepard_ascending.append(top_shepard[i][0])

    medin_ascending = []
    for i in range(len(top_medin)):
        medin_ascending.append(top_medin[i][0])

    print("Tversky Ascending in Similarity: " + str(tversky_ascending))
    print("Shepard Ascending in Similarity: " + str(shepard_ascending))
    print("Medin Ascending in Similarity: " + str(medin_ascending))