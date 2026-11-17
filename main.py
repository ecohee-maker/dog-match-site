from dataclasses import dataclass
from bakery import assert_equal
from drafter import *

set_website_style("daub")

@dataclass
class Dog:
    name: str
    activity_level: str
    needs_yard: bool
    size: str
    grooming_level: str
    description: str

DOG_DATABASE = [
    Dog("French Bulldog", "low", False, "small", "not much", "Playful, compact, and low-maintenance."),
    Dog("Chihuahua", "low", False, "small", "not much", "Sassy, loyal, and perfect for apartment living."),
    Dog("Basset Hound", "low", True, "medium", "some", "Gentle and easygoing with a great sense of smell."),
    Dog("Cavalier King Charles Spaniel", "low", False, "small", "a lot", "Affectionate lap dog with a silky coat."),
    Dog("Pug", "low", False, "small", "not much", "Charming, mischievous, and loving companion."),
    
    Dog("Corgi", "moderate", False, "small", "some", "Smart, alert, and surprisingly energetic for short legs."),
    Dog("Beagle", "moderate", True, "medium", "not much", "Friendly, curious, and great with families."),
    Dog("Golden Retriever", "moderate", True, "large", "a lot", "Intelligent, friendly, and devoted family dog."),
    Dog("Labrador Retriever", "moderate", True, "large", "not much", "Outgoing, active, and eager to please."),
    Dog("Cocker Spaniel", "moderate", False, "medium", "a lot", "Gentle, happy, and loves playtime."),
    
    Dog("Boxer", "moderate", True, "large", "not much", "Fun-loving, energetic, and protective companion."),
    Dog("Shih Tzu", "low", False, "small", "a lot", "Affectionate and happy house dog."),
    Dog("Boston Terrier", "moderate", False, "small", "not much", "Friendly, adaptable, and easy to train."),
    Dog("Dachshund", "moderate", False, "small", "not much", "Clever, lively, and courageous."),
    Dog("Poodle (Standard)", "high", True, "large", "a lot", "Exceptionally smart, active, and hypoallergenic."),
    
    Dog("German Shepherd", "high", True, "large", "some", "Confident, courageous, and highly trainable working dog."),
    Dog("Australian Shepherd", "high", True, "medium", "some", "Exuberant, work-oriented, and hyper-intelligent."),
    Dog("Border Collie", "high", True, "medium", "a lot", "The ultimate high-energy herd dog."),
    Dog("Siberian Husky", "high", True, "large", "some", "Athletic, outgoing, and loves cold weather activities."),
    Dog("Jack Russell Terrier", "high", False, "small", "not much", "Fearless, energetic, and compact powerpack."),
    # Low Activity Additions
    Dog("Greyhound", "low", True, "large", "not much", "Known as the '45-mph couch potato'—calm, gentle, and loves lounging."),
    Dog("Great Dane", "low", True, "large", "not much", "Patient, gentle giant that enjoys short walks and long naps."),
    Dog("Newfoundland", "low", True, "large", "a lot", "Sweet-tempered, devoted giant with a heavy coat that needs brushing."),
    Dog("Bernese Mountain Dog", "low", True, "large", "a lot", "Calm, affectionate, and good-natured cold-weather companion."),
    Dog("Bulldog (English)", "low", False, "medium", "not much", "Docile, willful, and friendly companion suited for relaxed homes."),
    Dog("Whippet", "low", False, "medium", "not much", "Quiet, affectionate, and loves sprinting briefly before napping."),
    Dog("Clumber Spaniel", "low", True, "large", "some", "Mellow, dignified, and affectionate gentleman of the spaniel family."),
    Dog("Maltese", "low", False, "small", "a lot", "Gentle, playful toy breed with a silky white coat."),
    Dog("Havanese", "low", False, "small", "some", "Cheerful, social, and adaptable little companion."),
    Dog("Pekingese", "low", False, "small", "a lot", "Independent, loyal lap dog with a regal mane."),

    # Moderate Activity Additions
    Dog("Bichon Frise", "moderate", False, "small", "a lot", "Playful, hypoallergenic, and peppy with a plush white coat."),
    Dog("Miniature Schnauzer", "moderate", False, "small", "some", "Obedient, spirited, and bearded little watchdog."),
    Dog("Shetland Sheepdog", "moderate", True, "small", "a lot", "Bright, eager, and playful miniature herding dog."),
    Dog("Basenji", "moderate", False, "small", "not much", "Fastidious, cat-like, and famous for not barking."),
    Dog("Brittany", "moderate", True, "medium", "some", "Bright, upbeat, and agile sporting companion."),
    Dog("Portuguese Water Dog", "moderate", True, "medium", "a lot", "Affectionate, adventurous, and curly-coated swimmer."),
    Dog("Standard Schnauzer", "moderate", True, "medium", "some", "High-spirited, smart, and reliable family protector."),
    Dog("Samoyed", "moderate", True, "medium", "a lot", "Gentle, adaptable, and famous for its 'Sammy smile' and fluffy coat."),
    Dog("Collie (Rough)", "moderate", True, "large", "a lot", "Devoted, graceful, and famously good with children."),
    Dog("Rottweiler", "moderate", True, "large", "not much", "Loyal, loving, and confident guardian."),

    # High Activity Additions
    Dog("Vizsla", "high", True, "large", "not much", "Affectionate, energetic 'velcro dog' built for runners."),
    Dog("Weimaraner", "high", True, "large", "not much", "Sleek, fearless, and athletic outdoor partner."),
    Dog("Dalmatian", "high", True, "large", "some", "Dignified, outgoing, and built for endurance running."),
    Dog("Belgian Malinois", "high", True, "large", "not much", "Intense, smart, and ultra-athletic working dog."),
    Dog("Rhodesian Ridgeback", "high", True, "large", "not much", "Dignified, even-tempered, and strong athletic hound."),
    Dog("German Shorthaired Pointer", "high", True, "large", "not much", "Enthusiastic, willing, and versatile outdoor athlete."),
    Dog("Nova Scotia Duck Tolling Retriever", "high", True, "medium", "some", "Smart, outgoing, and energetic retriever in a compact frame."),
    Dog("English Springer Spaniel", "high", True, "medium", "some", "Playful, polite, and eager-to-please field companion."),
    Dog("Miniature American Shepherd", "high", False, "small", "some", "Intelligent, self-motivated, and compact herding partner."),
    Dog("Papillon", "high", False, "small", "some", "Quick, curious, and surprisingly athletic agility star.")
]

@dataclass
class State:
    activity_level: str
    has_yard: bool | None
    preferred_size: str
    grooming_preference: str
    recommendations: list[Dog]

initial_state = State("", None, "", "", [])

@route
def index(state: State) -> Page:
    '''
    opens welcome page for dog match
    args: state -> current application state
    returns: welcome page
    '''
    return Page(
        state,
        [
            Header("Welcome to Dog Match! 🐶"),
            Text("Find the perfect dog breed for your lifestyle by answering a few quick questions."),
            Button("Start", start_quiz)
        ]
    )

@route
def start_quiz(state: State) -> Page:
    '''
    alters question 1 asking about activity level
    args: state (State): current app state
    returns: activity level question page with low, moderate, high
    '''
    return Page(
        state,
        [
            Header("Question 1: Activity Level"),
            Text("How active are you?"),
            Button("Low (Relaxed walks)", select_activity, {"choice": "low"}),
            Button("Moderate (Daily walks & playtime)", select_activity, {"choice": "moderate"}),
            Button("High (Running, hiking, constant action)", select_activity, {"choice": "high"}),
        ]
    )

@route
def select_activity(state: State, choice: str) -> Page:
    '''
    updates state with users activity level and goes to question 2
    args: state(State): current app state and choice (str): selcted activity level
    returns: yard access question page
    '''
    state.activity_level = choice
    return yard_question(state)

@route
def yard_question(state: State) -> Page:
    '''
    asks wether user has yard or not
    args: state (State): current app state
    returns: yard access page with yes/no buttons
    '''
    return Page(
        state,
        [
            Header("Question 2: Yard Access"),
            Text("Do you have a yard for the dog to run around in?"),
            Button("Yes", select_yard, {"choice": True}),
            Button("No", select_yard, {"choice": False}),
        ]
    )

@route
def select_yard(state: State, choice: bool) -> Page:
    '''
    updates state with user yard access and goes to question 3
    args: state(State): current app state and choice (bool): True is user has yard, False if not
    returns: Page: preferred dog size question
    '''
    state.has_yard = choice
    return size_question(state)

@route
def size_question(state: State) -> Page:
    '''
    renders question 3 asking user for preferred dog size
    args: state(State): current app state
    returns: Page: preferred size question with small, medium, and large buttons
    '''
    return Page(
        state,
        [
            Header("Question 3: Preferred Size"),
            Text("What size dog do you prefer?"),
            Button("Small", select_size, {"choice": "small"}),
            Button("Medium", select_size, {"choice": "medium"}),
            Button("Large", select_size, {"choice": "large"}),
        ]
    )

@route
def select_size(state: State, choice: str) -> Page:
    '''
    updates state with users preferred dog size and goes to question 4
    args: state(State): current app state and choice (str): selected dog size
    returns: Page: the grooming preference question page
    '''
    state.preferred_size = choice
    return grooming_question(state)

@route
def grooming_question(state: State) -> Page:
    '''
    renders question 4 asking how much grooming willing to do
    args: state(State): current app state
    returns: Page: grooming preference page with not much, some, a lot buttons
    '''
    return Page(
        state,
        [
            Header("Question 4: Grooming Preference"),
            Text("How much grooming are you willing to do?"),
            Button("A lot", select_grooming, {"choice": "a lot"}),
            Button("Some", select_grooming, {"choice": "some"}),
            Button("Not much", select_grooming, {"choice": "not much"}),
        ]
    )

@route
def select_grooming(state: State, choice: str) -> Page:
    '''
    updates state with users grooming preference and goes to results
    args: state (State): current app state and choice (str): selected grooming level
    returns: Page: recommendations page (or cat)
    '''
    state.grooming_preference = choice
    return recommendations(state)

def find_matching_dogs(state: State) -> list[Dog]:
    '''
    filters the DOG database for breeds that match the users preferences stored in state
    args: state(State): current app state containing user quiz questions
    returns: list[Dog]: list of dogs matching user preference
    '''
    matches = []
    for dog in DOG_DATABASE:
        if state.activity_level != "" and dog.activity_level != state.activity_level:
            continue
        if dog.needs_yard and state.has_yard is False:
            continue
        if state.preferred_size != "" and dog.size != state.preferred_size:
            continue
        if state.grooming_preference != "" and dog.grooming_level != state.grooming_preference:
            continue
        matches.append(dog)
    return matches

@route
def cat_recommendation(state: State) -> Page:
    '''
    renders alternative page suggesting cat with all least dog-like options
    args: state(State): current app state
    returns: Page: cate recommendation page with button to restart quiz
    '''
    return Page(
        state,
        [
            Header("Maybe You Should Get a Cat! 🐱"),
            Text("You selected low activity, no yard, small size, and minimal grooming!"),
            Text("If you want an independent companion that loves naps and low maintenance, a cat might be your ideal match."),
            Button("Start Over", restart_quiz)
        ]
    )

@route
def recommendations(state: State) -> Page:
    '''
    after reviewing user answers it will display what user matches best with
    args: state(State): current app state with completed quiz answers
    returns: Page: results page displaying matching dogs or cat page
    '''
    # Trigger Cat page if user picks all lowest-effort choices
    if (state.activity_level == "low" and 
        state.has_yard is False and 
        state.preferred_size == "small" and 
        state.grooming_preference == "not much"):
        return cat_recommendation(state)

    matching_dogs = find_matching_dogs(state)
    state.recommendations = matching_dogs
    
    content = [
        Header("Results: Your Dog Matches 🐶"),
        Text(f"Found {len(matching_dogs)} matching breed(s) based on your answers:")
    ]
    
    if len(matching_dogs) == 0:
        content.append(Text("No exact matches found! Try starting over with broader choices."))
    else:
        for dog in matching_dogs:
            content.append(Header(dog.name))
            content.append(Text(f"Size: {dog.size.capitalize()} | Grooming: {dog.grooming_level.capitalize()}"))
            content.append(Text(dog.description))
            
    content.append(Button("Start Over", restart_quiz))
    return Page(state, content)

@route
def restart_quiz(state: State) -> Page:
    '''
    resets user preferences and recommendations and returns to the wecome page
    args: state(State): current app state
    returns: Page: intial welcome page with cleared state
    '''
    state.activity_level = ""
    state.has_yard = None
    state.preferred_size = ""
    state.grooming_preference = ""
    state.recommendations = []
    return index(state)

from bakery import assert_equal

# 1. Test index (Welcome Page)
assert_equal(
    index(State("", None, "", "", [])),
    Page(
        State("", None, "", "", []),
        [
            Header("Welcome to Dog Match! 🐶"),
            Text("Find the perfect dog breed for your lifestyle by answering a few quick questions."),
            Button("Start", start_quiz)
        ]
    )
)

# 2. Test start_quiz (Question 1: Activity Level)
assert_equal(
    start_quiz(State("", None, "", "", [])),
    Page(
        State("", None, "", "", []),
        [
            Header("Question 1: Activity Level"),
            Text("How active are you?"),
            Button("Low (Relaxed walks)", select_activity, {"choice": "low"}),
            Button("Moderate (Daily walks & playtime)", select_activity, {"choice": "moderate"}),
            Button("High (Running, hiking, constant action)", select_activity, {"choice": "high"}),
        ]
    )
)

# 3. Test select_activity -> yard_question
assert_equal(
    select_activity(State("", None, "", "", []), "high"),
    Page(
        State("high", None, "", "", []),
        [
            Header("Question 2: Yard Access"),
            Text("Do you have a yard for the dog to run around in?"),
            Button("Yes", select_yard, {"choice": True}),
            Button("No", select_yard, {"choice": False}),
        ]
    )
)

# 4. Test yard_question directly
assert_equal(
    yard_question(State("low", None, "", "", [])),
    Page(
        State("low", None, "", "", []),
        [
            Header("Question 2: Yard Access"),
            Text("Do you have a yard for the dog to run around in?"),
            Button("Yes", select_yard, {"choice": True}),
            Button("No", select_yard, {"choice": False}),
        ]
    )
)

# 5. Test select_yard -> size_question
assert_equal(
    select_yard(State("high", None, "", "", []), True),
    Page(
        State("high", True, "", "", []),
        [
            Header("Question 3: Preferred Size"),
            Text("What size dog do you prefer?"),
            Button("Small", select_size, {"choice": "small"}),
            Button("Medium", select_size, {"choice": "medium"}),
            Button("Large", select_size, {"choice": "large"}),
        ]
    )
)

# 6. Test size_question directly
assert_equal(
    size_question(State("moderate", False, "", "", [])),
    Page(
        State("moderate", False, "", "", []),
        [
            Header("Question 3: Preferred Size"),
            Text("What size dog do you prefer?"),
            Button("Small", select_size, {"choice": "small"}),
            Button("Medium", select_size, {"choice": "medium"}),
            Button("Large", select_size, {"choice": "large"}),
        ]
    )
)

# 7. Test select_size -> grooming_question
assert_equal(
    select_size(State("high", True, "", "", []), "large"),
    Page(
        State("high", True, "large", "", []),
        [
            Header("Question 4: Grooming Preference"),
            Text("How much grooming are you willing to do?"),
            Button("A lot", select_grooming, {"choice": "a lot"}),
            Button("Some", select_grooming, {"choice": "some"}),
            Button("Not much", select_grooming, {"choice": "not much"}),
        ]
    )
)

# 8. Test grooming_question directly
assert_equal(
    grooming_question(State("low", True, "small", "", [])),
    Page(
        State("low", True, "small", "", []),
        [
            Header("Question 4: Grooming Preference"),
            Text("How much grooming are you willing to do?"),
            Button("A lot", select_grooming, {"choice": "a lot"}),
            Button("Some", select_grooming, {"choice": "some"}),
            Button("Not much", select_grooming, {"choice": "not much"}),
        ]
    )
)

# 9. Test select_grooming -> recommendations (with a known single match: Poodle (Standard))
poodle = Dog("Poodle (Standard)", "high", True, "large", "a lot", "Exceptionally smart, active, and hypoallergenic.")
assert_equal(
    select_grooming(State("high", True, "large", "", []), "a lot"),
    Page(
        State("high", True, "large", "a lot", [poodle]),
        [
            Header("Results: Your Dog Matches 🐶"),
            Text("Found 1 matching breed(s) based on your answers:"),
            Header("Poodle (Standard)"),
            Text("Size: Large | Grooming: A lot"),
            Text("Exceptionally smart, active, and hypoallergenic."),
            Button("Start Over", restart_quiz)
        ]
    )
)

# 10. Test recommendations when 0 matches are found
assert_equal(
    recommendations(State("high", False, "large", "a lot", [])),
    Page(
        State("high", False, "large", "a lot", []),
        [
            Header("Results: Your Dog Matches 🐶"),
            Text("Found 0 matching breed(s) based on your answers:"),
            Text("No exact matches found! Try starting over with broader choices."),
            Button("Start Over", restart_quiz)
        ]
    )
)

# 11. Test cat_recommendation route directly & via recommendations easter egg
assert_equal(
    cat_recommendation(State("low", False, "small", "not much", [])),
    Page(
        State("low", False, "small", "not much", []),
        [
            Header("Maybe You Should Get a Cat! 🐱"),
            Text("You selected low activity, no yard, small size, and minimal grooming!"),
            Text("If you want an independent companion that loves naps and low maintenance, a cat might be your ideal match."),
            Button("Start Over", restart_quiz)
        ]
    )
)

assert_equal(
    recommendations(State("low", False, "small", "not much", [])),
    Page(
        State("low", False, "small", "not much", []),
        [
            Header("Maybe You Should Get a Cat! 🐱"),
            Text("You selected low activity, no yard, small size, and minimal grooming!"),
            Text("If you want an independent companion that loves naps and low maintenance, a cat might be your ideal match."),
            Button("Start Over", restart_quiz)
        ]
    )
)

# 12. Test restart_quiz (resets state and returns index page)
assert_equal(
    restart_quiz(State("high", True, "large", "a lot", [poodle])),
    Page(
        State("", None, "", "", []),
        [
            Header("Welcome to Dog Match! 🐶"),
            Text("Find the perfect dog breed for your lifestyle by answering a few quick questions."),
            Button("Start", start_quiz)
        ]
    )
)

# 13. Test find_matching_dogs helper function directly
assert_equal(
    find_matching_dogs(State("high", True, "large", "a lot", [])),
    [poodle]
)
# Starts the Drafter web application
start_server(initial_state)





